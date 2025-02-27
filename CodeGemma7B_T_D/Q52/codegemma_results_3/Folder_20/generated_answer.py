def palindrome_of_length_n(text):
    text = text.lower()
    palindrome = set()
    for i in range(len(text) - 52):
        for j in range(i + 1, len(text) - 51):
            for k in range(j + 1, len(text) - 50):
                for m in range(k + 1, len(text) - 49):
                    for n in range(m + 1, len(text) - 48):
                        if text[i:i + 53] == text[i:i + 53][::-1]:
                            palindrome.add(text[i:i + 53])
    return palindrome