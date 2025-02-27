def palindrome_of_length_n(string):

    def is_palindrome(word):
        if len(word) != 474:
            return False
        for i in range(len(word) // 2):
            if word[i].lower() != word[len(word) - i - 1].lower():
                return False
        return True
    palindromes = set()
    for i in range(len(string) - 473):
        word = string[i:i + 474]
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes