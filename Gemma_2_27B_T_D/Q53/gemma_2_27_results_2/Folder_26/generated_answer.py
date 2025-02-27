def palindrome_of_length_at_least_n(text):
    pals = set()
    for i in range(len(text) - 31):
        for j in range(i + 32, len(text) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1]:
                pals.add(substring)
    return pals