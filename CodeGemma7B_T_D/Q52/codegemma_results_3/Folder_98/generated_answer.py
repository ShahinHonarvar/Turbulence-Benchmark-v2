def palindrome_of_length_n(text):
    low_text = text.lower()
    palindromes = set()
    for i in range(len(text) - 5):
        for j in range(i + 1, len(text) - 4):
            for k in range(j + 1, len(text) - 3):
                for l in range(k + 1, len(text) - 2):
                    for m in range(l + 1, len(text) - 1):
                        left = low_text[i:j + 1]
                        right = low_text[m:l + 1:-1]
                        if left == right:
                            palindromes.add(text[i:j + 1])
    return palindromes