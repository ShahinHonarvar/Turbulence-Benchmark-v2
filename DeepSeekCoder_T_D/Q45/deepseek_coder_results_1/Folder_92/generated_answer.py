def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[4:8])).lower()
    palindromes = set()
    n = len(letters)
    for i in range(1 << n):
        combination = ''.join((letters[j] for j in range(n) if i & 1 << j))
        if len(combination) >= 4:
            for k in range(len(combination) - 3):
                for l in range(k + 3, len(combination) + 1):
                    if is_palindrome(combination[k:l]):
                        palindromes.add(combination[k:l])
    return palindromes