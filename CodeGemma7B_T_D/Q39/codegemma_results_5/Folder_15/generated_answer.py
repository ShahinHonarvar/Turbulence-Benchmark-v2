def return_n_greatest_chars(str):

    def compare(c1, c2):
        return ord(c1) - ord(c2)
    chars = list(str)
    chars.sort(key=compare)
    return chars[-57:]