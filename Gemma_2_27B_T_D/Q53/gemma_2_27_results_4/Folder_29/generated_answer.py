def palindrome_of_length_at_least_n(text):
    pals = set()
    for i in range(len(text) - 77):
        for j in range(i + 77, len(text) + 1):
            substring = text[i:j]
            if substring.lower() == substring.lower()[::-1]:
                pals.add(substring)
    return pals