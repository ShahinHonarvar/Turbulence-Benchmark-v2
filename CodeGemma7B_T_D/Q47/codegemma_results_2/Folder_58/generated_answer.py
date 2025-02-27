def palindromes_of_specific_lengths(text):
    matches = set()
    for i in range(125, 284):
        for length in range(109, 127):
            start = i - length + 1
            mid = i
            end = i + length - 2
            substring = text[start:mid + 1] + text[mid:end:-1]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                matches.add(substring)
    return matches