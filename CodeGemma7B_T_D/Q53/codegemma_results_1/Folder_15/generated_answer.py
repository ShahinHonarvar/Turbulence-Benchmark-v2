def palindrome_of_length_at_least_n(text: str) -> set:
    text = text.lower()
    palindrome = set()
    while text != '':
        for i in range(len(text)):
            for j in range(i + 1, len(text)):
                if text[i:j + 1] == text[i:j + 1][::-1]:
                    palindrome.add(text[i:j + 1])
        text = text[:-1]
    return palindrome