def palindrome_of_length_at_least_n(text: str) -> set:
    seen = set()
    text = text.lower()
    for i in range(len(text) - 73):
        for j in range(i + 74, len(text) + 1):
            word = text[i:j]
            if word == word[::-1]:
                seen.add(word)
    return seen