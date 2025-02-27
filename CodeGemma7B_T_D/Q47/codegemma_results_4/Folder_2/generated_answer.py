def palindromes_of_specific_lengths(text):
    text = text.lower()
    results = set()
    for start in range(10, 60):
        for end in range(start + 18, start + 37):
            sub = text[start:end]
            if sub == sub[::-1] and sub.isalpha():
                results.add(sub)
    return results