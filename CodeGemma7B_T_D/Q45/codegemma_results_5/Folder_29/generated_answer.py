def palindromes_between_indices(text):
    text = text[2:9].lower()
    characters = list(set(text))
    palindromes = []
    for start in characters:
        for end in characters:
            if start != end:
                mid = start + (end - start) // 2
                palindrome = start + mid * 2 + end
                if palindrome in text:
                    palindromes.append(palindrome)
    return set(palindromes)