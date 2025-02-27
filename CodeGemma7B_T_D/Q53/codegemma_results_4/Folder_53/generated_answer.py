def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindrome_list = set()
    for i in range(len(text)):
        for j in range(i + len(palindrome_list), len(text)):
            palindrome = text[i:j + 1]
            if palindrome == palindrome[::-1] and len(palindrome) >= 64:
                palindrome_list.add(palindrome)
    return palindrome_list