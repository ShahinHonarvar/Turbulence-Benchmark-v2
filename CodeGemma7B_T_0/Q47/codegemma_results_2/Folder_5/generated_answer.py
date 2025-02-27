def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(63, 71):
        for j in range(i - 3, i + 1):
            if j - i + 1 in range(4, 6):
                if text[i:j + 1] == text[i:j + 1][::-1]:
                    palindromes.add(text[i:j + 1])
    return palindromes