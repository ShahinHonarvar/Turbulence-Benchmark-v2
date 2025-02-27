def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 96):
        for j in range(i + 96, len(text) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1]:
                result.add(text[i:j])
    return result