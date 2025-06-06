def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[2:10].lower()))
    palindromes = set()
    n = len(letters)
    for i in range(1 << n):
        subset = ''.join((letters[j] for j in range(n) if i & 1 << j))
        if len(subset) >= 4:
            for k in range(len(subset)):
                for l in range(k + 4, len(subset) + 1):
                    if is_palindrome(subset[k:l]):
                        palindromes.add(subset[k:l])
    return palindromes