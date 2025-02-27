def palindrome_of_length_at_least_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text) - 77):
        for j in range(i + 78, len(text) + 1):
            if text[i:j] == text[j - 1:i - 78:-1]:
                result.add(text[i:j])
    return result