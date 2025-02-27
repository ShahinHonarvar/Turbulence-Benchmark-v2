def palindrome_of_length_at_least_n(text):
    result = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            for k in range(j + 1, len(text)):
                if text[i] == text[j] == text[k]:
                    palindromes = text[i:j + 1]
                    if len(palindromes) >= 35:
                        result.add(palindromes)
    return result