def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(20, 75):
        for j in range(36, 43):
            start = i - j // 2
            end = i + j // 2 + (j % 2 == 0)
            if start < 0 or end >= len(text):
                continue
            if text[start:end + 1] == text[start:end + 1][::-1]:
                palindromes.add(text[start:end + 1])
    return palindromes