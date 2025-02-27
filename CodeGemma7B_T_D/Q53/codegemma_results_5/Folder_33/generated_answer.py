def palindrome_of_length_at_least_n(text):
    result = set()
    palindrome = ''
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            word = text[i:j].lower()
            palindrome = word
            if word == word[::-1] and len(word) >= 141:
                result.add(palindrome)
    return result