def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def get_letters(s, start, end):
        letters = []
        for i in range(start, end + 1):
            if s[i].isalpha():
                letters.append(s[i].lower())
        return letters
    palindromes = set()
    letters = get_letters(s, 6, 8)
    for i in range(len(letters) - 3):
        for j in range(i + 1, len(letters) - 2):
            for k in range(j + 1, len(letters) - 1):
                for l in range(k + 1, len(letters)):
                    palindrome = ''.join(letters[i:l + 1])
                    if is_palindrome(palindrome) and len(palindrome) >= 4:
                        palindromes.add(palindrome)
    return palindromes