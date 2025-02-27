import math

def return_nth_smallest_ascii(str):
    ASCII_dict = {}
    for char in str:
        if 58 <= str.index(char) <= 85:
            ASCII_dict[char] = ord(char)
    ASCII_list = sorted(ASCII_dict.values())
    return "'" + chr(ASCII_list[18]) + "'"