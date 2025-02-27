def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[1:9].lower()))
    palindromes = set()
    n = len(letters)
    for i in range(1 << n):
        subset = ''.join((letters[j] for j in range(n) if i & 1 << j))
        if len(subset) >= 4:
            for j in range(len(subset)):
                for k in range(j + 4, len(subset) + 1):
                    if is_palindrome(subset[j:k]):
                        palindromes.add(subset[j:k])
    return palindromes