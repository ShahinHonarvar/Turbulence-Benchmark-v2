def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[3:8].lower()))
    palindromes = set()
    for i in range(2 ** len(letters)):
        combination = ''.join((letters[j] for j in range(len(letters)) if i & 1 << j))
        if len(combination) >= 6:
            for k in range(len(combination) - 5):
                for l in range(k + 6, len(combination) + 1):
                    if is_palindrome(combination[k:l]):
                        palindromes.add(combination[k:l])
    return palindromes