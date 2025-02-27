def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindrome = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            temp = text[i:j + 1]
            if temp == temp[::-1] and len(temp) >= 24:
                palindrome.add(temp)
    return palindrome