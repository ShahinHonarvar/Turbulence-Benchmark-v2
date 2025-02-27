def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[0:8])).lower()
    palindromes = set()
    n = len(letters)
    for i in range(2 ** n):
        combination = ''.join((letters[j] for j in range(n) if i & 1 << j))
        for length in range(4, len(combination) + 1):
            for start in range(len(combination) - length + 1):
                substring = combination[start:start + length]
                if is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes