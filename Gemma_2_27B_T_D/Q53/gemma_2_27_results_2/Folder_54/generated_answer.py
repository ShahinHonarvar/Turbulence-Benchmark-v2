def palindrome_of_length_at_least_n(text):
    return {x for x in set([text[i:j] for i in range(len(text)) for j in range(i + 74, len(text) + 1)]) if x.lower() == x[::-1].lower()}