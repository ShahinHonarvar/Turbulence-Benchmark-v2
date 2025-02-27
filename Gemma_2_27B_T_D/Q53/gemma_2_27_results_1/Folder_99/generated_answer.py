def palindrome_of_length_at_least_n(text):
    return {p for p in [text[i:i + l] for l in range(115, len(text) + 1) for i in range(len(text) - l + 1)] if p.lower() == p[::-1].lower()}