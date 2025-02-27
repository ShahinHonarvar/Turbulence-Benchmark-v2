def palindromes_between_indices(text):
    text = text.lower()
    result = set()
    for i in range(len(text) - 2):
        for j in range(i + 1, len(text) - 1):
            for k in range(j + 1, len(text)):
                if text[i] in 'abcdefghijklmnopqrstuvwxyz' and text[j] in 'abcdefghijklmnopqrstuvwxyz' and (text[k] in 'abcdefghijklmnopqrstuvwxyz'):
                    if text[i] == text[j] and text[j] == text[k]:
                        result.add(text[i] + text[j] + text[k])
    return result