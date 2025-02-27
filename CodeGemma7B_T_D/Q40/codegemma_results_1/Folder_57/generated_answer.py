def return_n_smallest_chars(given_str):
    """
            This function takes one argument, a string of distinct characters and creates a
            list of exactly 29 characters of the given string that have the smallest ASCII
            values. The function should sort the list in descending order and returns the list.
            """
    ascii_values = [ord(char) for char in given_str]
    ascii_values.sort()
    smallest_chars = [chr(ascii_value) for ascii_value in ascii_values[:29]]
    smallest_chars.sort(reverse=True)
    return smallest_chars

def main():
    given_str = input('Enter a string of distinct characters: ')
    smallest_chars = return_n_smallest_chars(given_str)
    print('The 29 characters with the smallest ASCII values are:', smallest_chars)