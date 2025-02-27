def palindromes_between_indices(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 4):
        for j in range(i + 1, len(text) - 3):
            for k in range(j + 1, len(text) - 2):
                for l in range(k + 1, len(text) - 1):
                    for m in range(l + 1, len(text)):
                        if text[i] in 'abcdefghijklmnopqrstuvwxyz' and text[j] in 'abcdefghijklmnopqrstuvwxyz' and (text[k] in 'abcdefghijklmnopqrstuvwxyz') and (text[l] in 'abcdefghijklmnopqrstuvwxyz') and (text[m] in 'abcdefghijklmnopqrstuvwxyz'):
                            if text[i:j + 1] == text[j:i - 1:-1]:
                                palindromes.add(text[i:j + 1])
    return palindromes