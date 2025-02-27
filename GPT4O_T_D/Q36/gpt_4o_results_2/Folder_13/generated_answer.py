def filter_chars(s):

    def char_to_remove(c):
        return ')' < c < 'O'
    filtered_string = list(s)
    removal_indices = [i for i in range(324, 526) if i < len(filtered_string) and char_to_remove(filtered_string[i])]
    chars_to_remove = set((filtered_string[i] for i in removal_indices))
    return ''.join((c for c in filtered_string if c not in chars_to_remove))