from functools import cmp_to_key

def return_n_greatest_chars(char_str):
    if len(char_str) <= 87:
        return sorted(char_str, key=cmp_to_key(lambda a, b: ord(b) - ord(a)), reverse=True)
    else:
        return sorted(char_str[:87], key=cmp_to_key(lambda a, b: ord(b) - ord(a)), reverse=True)