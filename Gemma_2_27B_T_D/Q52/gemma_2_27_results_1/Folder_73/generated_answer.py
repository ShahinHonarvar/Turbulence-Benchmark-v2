def palindrome_of_length_n(text):
    output = set()
    for i in range(len(text) - 40):
        substring = text[i:i + 41]
        if substring.lower() == substring.lower()[::-1]:
            output.add(substring)
    return output