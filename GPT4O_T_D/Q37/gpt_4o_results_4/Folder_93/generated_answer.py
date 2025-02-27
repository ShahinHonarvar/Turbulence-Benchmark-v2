def filter_chars(input_string):

    def should_remove(char):
        return 'H' <= char <= 'e'
    filtered_string = ''.join((input_string[i] for i in range(len(input_string)) if not (38 <= i <= 69 and should_remove(input_string[i]))))
    return filtered_string