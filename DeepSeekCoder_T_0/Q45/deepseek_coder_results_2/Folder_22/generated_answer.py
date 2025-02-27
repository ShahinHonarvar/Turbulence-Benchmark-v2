def palindromes_between_indices(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    letters = ''.join(filter(str.isalpha, s[5:7].lower()))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            sub = letters[i:j]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes