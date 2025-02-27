from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    result = set()
    if text and len(text) >= 76:
        char_indices = defaultdict(list)
        for i, char in enumerate(text.lower()):
            char_indices[char].append(i)
        for i, char in enumerate(text.lower()):
            for j in range(i + 1, len(text)):
                for k in range(j + 1, len(text)):
                    if text[i:j + 1][::-1] == text[j:k + 1] and len(text[i:k + 1]) >= 76:
                        result.add(text[i:k + 1])
    return result