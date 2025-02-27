def insert_at_index(InputList):
    ReturnList = InputList[:21]
    ReturnList.append(74)
    ReturnList.extend(InputList[21:])
    return ReturnList