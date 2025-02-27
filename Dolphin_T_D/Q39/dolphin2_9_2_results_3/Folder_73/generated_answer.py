def return_n_greatest_chars(s):
    """
    Write a function called 'return_n_greatest_chars' that takes one argument, a string of distinct characters and creates the sorted list of exactly 80 characters of the given string that have the greatest ASCII values. The function should sort the list in ascending order and returns it.
    """
    char_values = sorted([(ord(ch), ch) for ch in set(s)], reverse=True)
    return [ch for _, ch in char_values[:80]]