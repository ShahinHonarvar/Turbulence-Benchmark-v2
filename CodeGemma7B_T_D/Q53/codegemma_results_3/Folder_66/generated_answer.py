def palindrome_of_length_at_least_n(text):
    result = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i, len(text)):
            current_word = text[i:j + 1]
            current_word = current_word.strip()
            if current_word.isalpha() and len(current_word) >= 76 and (current_word == current_word[::-1]):
                result.add(current_word)
    return result