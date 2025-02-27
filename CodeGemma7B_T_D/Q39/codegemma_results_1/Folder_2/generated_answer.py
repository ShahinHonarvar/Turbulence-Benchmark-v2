def return_n_greatest_chars(char_string):
    char_tuples = [(char, ord(char)) for char in char_string]
    sorted_tuples = sorted(char_tuples, key=lambda tup: tup[1])
    greatest_tuples = sorted_tuples[-48:]
    return [tup[0] for tup in greatest_tuples]