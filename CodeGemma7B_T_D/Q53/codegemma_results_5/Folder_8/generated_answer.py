def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            palindrome = text[i:j]
            if palindrome == palindrome[::-1] and len(palindrome) >= 45 and palindrome.isalpha():
                result.add(palindrome)
    return result