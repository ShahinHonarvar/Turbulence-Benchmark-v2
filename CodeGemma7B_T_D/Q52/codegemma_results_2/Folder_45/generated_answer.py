def palindrome_of_length_n(text):
    palindrome_list = []
    modified_text = text.lower()
    text_length = len(modified_text)
    for i in range(text_length):
        for j in range(i, text_length):
            substring = modified_text[i:j + 1]
            if substring == substring[::-1] and len(substring) == 21 and substring.isalpha():
                palindrome_list.append(substring)
    return set(palindrome_list)