def insert_before_character(mystring):
    listofcharacters = [c for c in mystring]
    for i in range(len(listofcharacters)):
        if listofcharacters[i] == 'a':
            listofcharacters.insert(i, 'A')
    newstring = ''.join(listofcharacters)
    return newstring