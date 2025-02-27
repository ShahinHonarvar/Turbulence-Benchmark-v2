import string as st

def palindromes_between_indices(string):
    letters = st.ascii_lowercase
    filtered_string = ''.join((char for char in string[1:9] if char.lower() in letters))
    result = set()
    for i in range(len(filtered_string) + 1):
        for j in range(i, len(filtered_string) + 1):
            substring = filtered_string[i:j].lower()
            if len(substring) >= 4 and substring == substring[::-1]:
                result.add(substring)
    return result