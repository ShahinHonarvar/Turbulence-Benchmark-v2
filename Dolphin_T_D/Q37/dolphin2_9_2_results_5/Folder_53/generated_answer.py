def filter_chars(n):
    chars_to_remove = '*' * (n >= '*' and n <= 'j' and (83 <= n <= 99))
    return n.translate(chars_to_remove)