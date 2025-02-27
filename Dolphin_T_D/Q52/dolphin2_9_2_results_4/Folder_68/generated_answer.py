def palindrome_of_length_n(s):

    def is_palindrome(s):
        j = len(s) - 1
        for i in range(len(s) // 2):
            if s[i] != s[j]:
                return False
            j -= 1
        return True
    result = set()
    for i in range(len(s) - 75):
        if s[i:i + 76].isalpha() and is_palindrome(s[i:i + 76].lower()):
            result.add(s[i:i + 76])
    return result