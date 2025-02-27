def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[5:10].lower()))
    palindromes = set()
    for i in range(2 ** len(letters)):
        combination = ''.join((letters[j] for j in range(len(letters)) if i & 1 << j))
        if len(combination) >= 6:
            for j in range(len(combination) - 5):
                for k in range(j + 6, len(combination) + 1):
                    if is_palindrome(combination[j:k]):
                        palindromes.add(combination[j:k])
    return palindromes