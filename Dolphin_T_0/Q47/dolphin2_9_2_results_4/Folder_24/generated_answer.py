def palindromes_of_specific_lengths(text):
    text = text[11:92].lower()
    return set((text[i:i + length] for i in range(len(text) - length + 1) for length in range(42, 78) if text[i:i + length] == text[i:i + length][::-1]))