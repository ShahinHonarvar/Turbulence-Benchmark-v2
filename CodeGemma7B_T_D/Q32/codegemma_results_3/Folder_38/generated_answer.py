def insert_after_character(str):

    def f(c):
        if c == ord('X'):
            return 'X6'
        return chr(c)
    return ''.join((f(ord(c)) for c in str))