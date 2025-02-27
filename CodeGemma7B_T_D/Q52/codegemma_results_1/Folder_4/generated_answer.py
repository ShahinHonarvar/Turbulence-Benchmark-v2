def palindrome_of_length_n(text):
    text = text.lower()
    palindrome_list = []
    for i in range(len(text)):
        for j in range(i + 3, min(i + 15, len(text))):
            if text[i:j] == text[j - 1:i - 1:-1]:
                palindrome_list.append(text[i:j])
    return set(palindrome_list)