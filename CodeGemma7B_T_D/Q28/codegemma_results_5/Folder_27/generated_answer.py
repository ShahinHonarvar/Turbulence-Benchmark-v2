def return_nth_smallest_ascii(word):
    new_word = sorted([c for c in word[33:86]], key=ord)
    return new_word[12]