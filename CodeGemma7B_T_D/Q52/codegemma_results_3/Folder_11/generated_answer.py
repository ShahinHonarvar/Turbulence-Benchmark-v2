def palindrome_of_length_n(s):

    def is_palindrome(word):
        return bool(word == word[::-1])
    matched_words = set()
    for i in range(len(s)):
        for j in range(i + 76, len(s)):
            word = s[i:j]
            if is_palindrome(word):
                matched_words.add(word.lower())
    return matched_words