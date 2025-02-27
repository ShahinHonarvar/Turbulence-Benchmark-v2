def filter_chars(input_string):
    filtered_string = []
    for char in input_string:
        if char in string.ascii_uppercase:
            if char > '%' and char < 'q':
                filtered_string.append(char)
    return ''.join(filtered_string)

def main():
    input_string = input('Enter a string: ')
    filtered_string = filter_chars(input_string)
    print('Filtered string:', filtered_string)