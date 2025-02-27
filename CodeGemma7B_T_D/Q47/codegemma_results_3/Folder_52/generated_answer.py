def palindromes_of_specific_lengths(text):
    found_palindromes = set()
    text = text.lower()
    for i in range(44, 100):
        for j in range(i, 99 + 1):
            current_substring = text[i:j + 1]
            if current_substring == current_substring[::-1] and len(current_substring) in range(13, 43):
                found_palindromes.add(current_substring)
    return found_palindromes